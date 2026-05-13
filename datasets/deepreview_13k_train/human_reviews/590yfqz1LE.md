# Measuring Non-Adversarial Reproduction of Training Data in Large Language Models

- Decision: Accept
- Scores: 6, 5, 8, 8, 8, 6, 5, 8

## Abstract
Large language models memorize parts of their training data. Memorizing short snippets and facts is required to answer questions about the world and to be fluent in any language. But models have also been shown to reproduce long verbatim sequences of memorized text when prompted by a motivated adversary. In this work, we investigate an intermediate regime of memorization that we call non-adversarial reproduction, where we quantify the overlap between model responses and pretraining data when responding to natural and benign prompts. For a variety of innocuous prompt categories (e.g., writing a letter or a tutorial), we show that up to 15% of the text output by popular conversational language models overlaps with snippets from the Internet. In worst cases, we find generations where 100% of the content can be found exactly online. For the same tasks, we find that human-written text has far less overlap with Internet data. We further study whether prompting strategies can close this reproduction gap between models and humans. While appropriate prompting can reduce non-adversarial reproduction on average, we find that mitigating worst-case reproduction of training data requires stronger defenses—even for benign interactions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work discusses the case of unintentional reproduction of training data by large language models. While most of the literature discusses an adversarial nature of prompting to extract training data, this work tries to quantify how frequently this influence happens in a non-adversarial situation. One of the findings of the work is that non-adversarial reproduction is much higher in expository tasks than in creative ones, and even prompting techniques, while they can reduce the average reproduction rate, are not sufficient to prevent longer sequences from appearing. One of the highlight results of this work is that about 15% of the text output by popular conversation language models overlaps with short snippets of text on the internet, much higher than baseline rates by humans on the same task.

### Strengths
Overall, this paper was a joy to read. I found it to be very thoughtfully written. I routinely ended up in situations where I had a particular thought experiment in mind, and the next section showed just that set of ablations or experiments.

- I liked Figure 4(b) which shows how reproduction strongly depends on the task. This consolidates an important finding/hypothesis. At a high level, while the paper reports that 8-15% of LLM-generated text overlaps with existing online snippets, it goes further to analyze the types of overlaps. This also highlights the complexity of defining "problematic" reproduction.
- I found the experiment on extracting Quotations quite interesting, in particular, because it shows incorrect attribution of the quote.
- Distribution of overlap lengths: A small percentage of outputs contain very long reproduced sequences. This long-tail phenomenon suggests that even with low average reproduction rates, LLMs can still pose risks in specific cases.

### Weaknesses
 - Frequency of Reproduced Sequences: The paper could benefit from clarifying how often the reproduced sequences appear within their training data proxy, AUXDATASET. Understanding whether these snippets are rare or commonly encountered would help contextualize the reproduction risks.

- Justification of 50-Character Threshold: The choice of a 50-character threshold to define reproduced sequences is not fully justified. In particular, this is quite different from past work. While some examples in the Appendix suggest that 50 characters is a meaningful number, I believe most examples highlight that such sequence lengths can be so common in the natural language distribution that their reproduction does not matter. Further explanation would help readers assess whether this threshold adequately captures the difference between common phrases and more problematic reproductions.

- Data in Figure 2(b): Figure 2(b) appears to have only partial bar plots for some models (Llama and GPT), making the comparison across models less robust. Or am I missing something here?

Overall, I am constantly battling between thinking that 50 characters is too less, and then seeing the argument that these reproduction rates are much higher than humans. This makes me wonder if humans are the right baseline here. Would a human with a passage (RAG style reading comprehension) be a better baseline? There is a qualitative dichotomy here: the 50 characters do not feel meaningful when visualized, yet stay higher than what a human would reproduce.

### Questions
Please refer to sections above and answer the questions

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper tackles the problem of mitigating non-adversarial training data reproduction (natural and benign prompts from users revealing training data verbatim) in LLMs. The experiments find that in some cases as much as 15% of text output by LLMs overlaps with moderate snippets (40-60 characters) of the Internet. A comparative analysis finds that human-written text has far less overlap compared to LLM generated text. The paper proposes prompting strategies to close this human and LLM gap. Though these strategies close the gap between LLMs and humans on average, the paper suggests that worst-case reproduction might need stronger adversarial defenses.

The classes of tasks chosen for LLM text generation in this paper can be broadly classified into *creative writing*, *expository writing*, and *argumentative writing*. Since training data information is not available for certain models, the training data is approximated by collecting a large dataset of Web content (AUXDATASET).

The primary metric used is overlap rate (the percentage of characters in each generation that belong to a substring of at least 50-consecutive characters found exactly in AUXDATASET).

### Strengths
The paper is an extensive analysis of situations where LLMs generate text from training data verbatim, even when not explicitly prompted to reveal such information. The later case has been seen in adversarial attacks against LLMs in recent research. So, the results from this study can be used to inform us about scenarios where data leakage happens without explicit adversarial effort.

### Weaknesses
The current text is ordered as a set of subsections with a verbatim description of experimental steps. The presentation lacks focus on the main contributions of this research. For example, if this is the case, it should probably be highlighted that LLM data leakage studies for benign prompts haven't been looked at. Furthermore, instead of presenting all the results (as in Section 3) as small headings and text, it would help to have an additional small section which highlights the most important contributions which readers can take away from the paper.

I have some concerns about the collection of human data regarding plagiarism and contamination. Please refer to the Questions section.

### Questions
1. (Line 162 - Question about human-written baseline) Even with this measure of choosing content after LLM cut-off date and content which is not part of AUXDATASET, how is it confirmed that the content taken from Reddit is not LLM generated? Is it not possible that an LLM might have been used to generate it?

2. (Line 321) The paper mentions, “We find that LLMs reproduce more existing data than humans, except when humans do blatant plagiarism.” I might have missed it in the text, but it would be great to have some clarification regarding how this is controlled? For example, given a prompt like “Write a tutorial about setting up an Nginx server.”, humans might be prone to copy data verbatim from top-ranked articles on a search engine. There is a discussion in Line 404 about IMDb reviews, but what measures were taken for Reddit content?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper shows how language models can reproduce training data even with 'non-adversarial' prompts. While LLMs have been previously shown to reproduce training data, these experiments were conducted with adversarial assumptions, and the prompts used can be considered a violation of user policy by many LLM developers. The authors argue that even under the assumption of non-adversarial prompts, i.e., everyday use prompts that are not targeted at extracting training data, one can see LLMs regurgitating their training data. The authors provide a wide range of experiments on many different SOTA conversational LLMs and with many different categories of prompts to support their hypothesis.

### Strengths
- Incredibly relevant work. While the pessimist in me believes that LLM developers will always find new excuses to argue why LLMs regurgitating sensitive or proprietary data is not their responsibility, it is important to try and keep holding them accountable. In the context of adversarial reproduction of training data not being "typical or allowed user activity", this work plays an important role in highlighting how even everyday use of LLMs can reproduce training data.
- Wide range of experiments, both in terms of different models, as well as verifying various hypotheses. Lots of interesting insights.
- Qualitative analysis and handpicked examples. I was happy to see some qualitative analysis by the authors, especially of the long tail.

### Weaknesses
 - The use of a 50-character limit for overlap rate. I'm not convinced that the 50-character limit is strong enough to cause issues for LLMs reproducing training data. I'm not familiar with legal precedence on reproducing text without attribution; but at least when quoting from other sources, the limits are usually looser - even the strictest being around 25-50 words and usually, it is a few hundred words (https://ogc.harvard.edu/pages/copyright-and-fair-use, https://stevelaube.com/how-much-can-i-quote-from-another-source-without-permission/). Although, it should be mentioned that the authors are very open about their overall results and also discuss the long-tailed part of the reproduction, which highlights some actual issues. But despite this, their main results and trends are focused on an overlap rate defined with a 50-character limit.
- Lack of details on additional prompts used in the experiments. The authors have created some manual human-written prompts, which are used alongside data scraped from Reddit, in their experiments. I understand that releasing all these prompts during the reviewing phase might not be practical, and I appreciate the authors mentioning that they will release them in a later version of the paper, but I would like to see some details in the paper to perform a proper review of their work. More details on this in the questions below.

### Questions
- Can the authors reason why the 50-character limit beyond simply the argument that non-adversarial prompts reproduce less training data? The qualitative analysis of those 50-character snippets is appreciated, but as the authors showed, many of them are common phrases that might not constitute problematic behaviour from LLMs.
- Can the authors provide more details on how their manual prompts were created? Were they crowdsourced, or written by the authors themselves? Were they sourced from how authors themselves commonly use LLMs, or were they thought up in bulk at once? Were there efforts made to categorize them into a variety of prompts (beyond the three broad categories used in the paper), or maybe efforts made to check this variety after the prompts were created? No answers are bad answers here, even if the prompts were written by the authors in bulk in one sitting to capture the broad categories defined, that's a good start. But in any case, details are needed.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores to what degree LMs reproduce their training data in natural circumstances, i.e. settings where there is no adversarial pressure to reproduce the text. Human-written text is used to compare the extent to which the completions have exact matches in AuxDataset. The results show that unintended reproduction occurs more if the text is generated by models instead of humans, and if the task is expository, e.g. tutorials. Two system prompts are  investigated for mitigating unintended reproduction, yielding moderate success.

### Strengths
1) The paper is well-written and accessible. The figures effectively convey the key findings.
2) The empirical results are extensive and presented in a way that is easy to interpret. The authors test the most relevant models (including GPT, Claude, and Llama) and use varied datasets including real conversations.
3) The experiments are well-designed, the knowledge cutoffs and dataset limitations are addressed in the text.

### Weaknesses
1) Only exact matches are considered, excluding reproduction of close matches with a low hamming-distance or reproduction of semantics.
2) The results are harder to interpret due to the possibility that a large number of reproductions by both humans and models is not captured by using AuxDataset. Perhaps the extent of the problem could be estimated by running the tests on a dataset that is expanded with additional sources and comparing the resulting numbers to the current ones.
3) The selection of 50 character length seemed insufficiently motivated. Especially since it is different from the prior work and results in both memorised and unoriginal phrases being included.

### Questions
1) Are strings of length 40-60 (Line 45) or 50 (Line 129) considered?
2) Do the reproductions occur in similar contexts to the originals?
3) Lines 162-164 - what is the filtering procedure for the human-written text for it to not appear on the internet? If it is filtered, how did plagiarism appear in the human-written IMDb reviews?

Nitpicks:
1) Figure 1 could be improved by adjusting the colour scheme and ensuring the readability of the small text.
2) The use of “aligned” in section 5 could be more precise. While Christiano et al., 2017 and Ouyang et al., 2022 describe alignment as a continuous objective of RLHF fine-tuning, Nasr et al. (2023) simply uses “aligned” to describe models that have undergone RLHF. To avoid this ambiguity, more specific terms like “RLHF-tuned” or “alignment fine-tuned” could be used to describe these models.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper measures character-level verbatim text produced by LLMs (GPT, Claude, and Llama) on benign prompts and conversations, in contrast to adversarial membership inference attacks. The authors find that LLMs indeed reproduce internet text up to 15% of the time (50+ characters), in the worst case regurgitating over 1000 characters. The authors provide a breakdown of severity by task and compare to human baselines. Finally, the authors find that setting a system prompt can reduce this form of text reproduction for shorter sequences.

### Strengths
Significance: This paper is interesting because it quantifies the known phenomenon of LLMs reproducing text from their training data. In contrast to prior work, it attempts to evaluate a natural distribution of reproduced text lengths. The topic is important as LLMs are commonly used as assistants: there is a quantified risk to using LLMs for writing and code generation, as training data reproduction could result in unintentional plagiarism from the end user. This is exemplified by one of the most interesting findings of this paper is that benign prompting can result in reproduced text of 100 characters (2.5% of the time) and 1000 characters (0.01% of the time).

Quality: The authors conduct extensive analysis to break down the reproduction by text category and also demonstrate that reproduction rate is higher than human written text, including qualitative analysis and a simple mitigation strategy, with a clear presentation of their findings.

### Weaknesses
1. 50 character cutoff may overestimate regurgitation: The authors acknowledge this limitation, but it is difficult to differentiate based on character length alone whether the data is truly regurgitated off the internet or just due to it being a common phrase, especially when the length is around 50 characters. Additional analysis to estimate a numerical proportional breakdown between these two categories would make the paper more rigorous. There is far less doubt about text reproduction vs. common phrases past the 100-150 character point.

2. AI contaminated human baselines: Since the human baselines were scraped off the internet after the training cutoff of these models, they could already contain AI generated text from a prior generation of LLMs rather than represent a natural distribution of human writing. I would find it interesting if you can also evaluate the reproduction length distribution of human data known to be mostly free from AI contamination, i.e. before the widespread release of LLM assistants.

### Questions
1. How fast can you check whether a given generation is in AuxDataset? Curious if we can reduce the probability of regurgitating very long text by doing a check against an internet proxy dataset at inference time.

2. It's very interesting that the system prompt you used below reduces reproduction length. Why do you think this works? Did you try any other system prompts outside of this and the Claude prompt? Is it because the model can internally model a circuit to determine the probability of text being in its training data? If this is the case, it's even more interesting that this works nearly just as well for the smaller Llama 8B model as the larger 405B model, especially since the 8B model is expected to have weaker internal circuits.

Prompt: ```Your primary goal is to produce content that is completely original and free from any existing text on the Internet. This means that if someone were to take a few words from your explanation and search for them online, they can not find any matching results.```

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates non-adversarial reproduction in Large Language Models, where models unintentionally reproduce strings of their training data in response to benign prompts. By analyzing various tasks including creative writing and expository writing, the authors found that 10%-15% of LLM-generated content overlaps with internet text, significantly more than human-generated text. The study shows that expository tasks are especially prone to this phenomenon. Although specific prompting strategies can reduce the frequency of reproduced content, they do not fully prevent long sequences from appearing, indicating a need for stronger measures to mitigate unintended data leakage.

### Strengths
1. This paper studies a very interesting question about quantifying non-adversarial reproduction in LLMs, which is practical in using LLMs.

2. The analysis of the question is comprehensive, containing the conclusion for different tasks. The study provides a good understanding of how and when LLMs are more likely to reproduce training data.

3. The exploration of prompting as a mitigation strategy gives good insights, showing both its potential and limitations.

### Weaknesses
1. The evaluation results might be biased because the authors cannot access the real training dataset of evaluated LLMs. 

2. Some points in the paper are not very clear. For example, for the prompt mitigating part, the authors do not demonstrate which dataset are they using. And since they can use WildChat or LMSYS-Chat-1M, what is the motivation for collecting a new dataset?

3. The length of substrings that are used to calculate the overlap rate is strange. This paper considers a substring of 50 words, which is 'shorter than the 50 token (150–200 characters) threshold used in previous studies on adversarial extraction'. However, the authors do not provide a decent reason for using 50 words. The authors also mention that a substring of 50 words could be both common or unique sentences. However, I do not think a common sentence or phrase should be considered as a leakage of training data. Using such a standard could make the evaluation results further biased.

### Questions
1. Why do the authors not consider open-source LLMs where they can know which datasets are used for training? For example, in the Membership Inference Attack area of LLMs, researchers usually use Pythia and the Pile dataset.

2. Why do the authors collect their own dataset instead of WildChat and LMSYS-Chat-1M? What is the unique advantage of the new dataset?

3. Why do the authors consider substrings of 50 words? How will the results change if changing the threshold?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors investigate the issue of non-adversarial reproduction, which refers to the overlap between LLM outputs in response to natural prompts (mainly writing prompts) and internet text. The authors argue that LLM-generated text carries a higher risk of overlapping with internet text than human-written text. Additionally, the authors explore the preliminary use of prompt design to reduce overlap.

### Strengths
1. Non-adversarial reproduction is valuable for protecting LLM outputs from risks such as infringement and privacy violations.
  
2. The authors validate the existence of non-adversarial reproduction risks across several mainstream models.

### Weaknesses
1. The authors’ conclusion seems somewhat obvious, as LLMs are explicitly fit on internet text. Intuitively, LLMs are more likely to produce text resembling their training corpus than humans. The authors should better articulate the value of their findings. Specifically, the paper lacks a deeper analysis of why the observed overlap is significant beyond the fact that LLMs are trained on internet text. A more thorough discussion of the implications of this overlap, such as potential copyright issues or the perpetuation of biases present in the training data, would strengthen the paper's contribution.

2. Building on the first point, the authors propose using prompt design to mitigate overlap. However, the method and its underlying principles lack significant innovation. The paper does not explore more sophisticated techniques for reducing overlap, such as fine-tuning or adversarial training. The proposed prompt design approach seems like a basic attempt and does not delve into the nuances of how different prompt structures or constraints might affect the level of reproduction.

3. The authors appear to conflate reproduction of internet text and training data. These are not equivalent, as the training data depends on the model's degree of fit. Especially when using a simulated dataset, this discrepancy may be amplified. The paper should clarify the distinction between the general internet text and the specific subset of data used for training the models. The analysis should also consider the potential for variations in the degree of overlap based on the model's training regime and the specific data it was trained on.

4. The task is limited to writing. I suggest the authors consider extending it to other tasks. Generally, open-ended writing tasks are more likely to lead LLMs to recite memorized training data. The paper should explore other tasks, such as code generation or mathematical reasoning, to determine if the observed overlap is specific to text generation or a more general phenomenon across different types of LLM outputs. This would provide a more comprehensive understanding of the issue.

### Questions
1. I suggest that the authors consider using some training data detection methods (e.g., [1]) to assist in identifying training corpus when exploring reproduction of training data.

[1] Detecting Pretraining Data from Large Language Models. (ICLR-24)

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 8

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the problem of "non-adversarial production of training data", which is the problem of "how often do LLM copy the training data on normal user prompts?". The authors craft some tasks and used two existing user prompts datasets, and use the datasets to check for overlap between the LLM outptus and their training dataset. Since their actual training dataset is unknown, they instead of a webscale corpus: AuxDataset, as a proxy. Their result shows that 5%-15% of LLM outputs are reproduction of training data. They have tested with using prompts to mitigate this problem, and they show that prompts can reduce the reproduction rate, but can not prevent long-tail leakage of training data.

### Strengths
- The motivation of this paper is clear and specific. This paper propose a new threat "non-adversarial reproduction of training data".
- This paper provides solid experiments across a large range of LLMs.
- This paper creates a new task dataset, and propose a method to evaluate the human reproduction baseline, to evaluate the human reproduction baseline, they collect a human benchmark dataset.
- This papaer is well written, easy to follow and understand.

### Weaknesses
 - In section 6, you mentioned that it's hard to distinguish reproduction of common idioms from problematic memorization. Is it possible to estimate how much of the overlap is problematic? Cause sometimes citing a known source is not a problem, so that may not be considered a problematic reproduction.
- You have tested on temperature of 0 and 0.7, both are low temperature. Can you add experiments on temperature higher than 1 to see the reproduction rate under high temperature?
- You have tested two system prompts in section 4, can you test with more prompts?

### Questions
- In the **human-written text dataset**, how do you make sure that the human-written texts are not actually generated by an LLM? Cause human may use LLM to generate these texts.

### Soundness
3

### Presentation
3

### Contribution
3
