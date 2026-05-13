# Detecting Pretraining Data from Large Language Models

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Although large language models (LLMs) are widely deployed, the data used to train them is rarely disclosed. 
Given the incredible scale of this data, up to trillions of tokens, it is all but certain that it includes potentially problematic text such as copyrighted materials, personally identifiable information, and test data for widely reported reference benchmarks. 
However, we currently have no way to know which data of these types is included or in what proportions. 
In this paper, we study the pretraining data detection problem: \textit{given a piece of text and black-box access to an LLM without knowing the pretraining data, can we determine if the model was trained on the provided text?}  
To facilitate this study, we introduce a dynamic benchmark \data that uses data created before and after model training to support gold truth detection. We also introduce a new detection method \model based on a simple hypothesis: an unseen example is likely to contain a few outlier words with low probabilities under the LLM, while a seen example is less likely to have words with such low probabilities. 
\model can be applied without any knowledge about the pretraining corpus or any additional training, departing from previous detection methods that require training a reference model on data that is similar to the pretraining data.
Moreover, our experiments demonstrate that \model achieves a 7.4\% improvement on \data  over these previous methods.
We apply \model to three real-world scenarios, copyrighted book detection, contaminated downstream example detection and privacy auditing of machine unlearning, and find it a consistently effective solution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to detect training data in LLMs, based on the assumption of "an unseen example tends to contain a few outlier words with low probabilities, whereas a seen example is less likely to contain words with such low probabilities." Experiments on one wiki dataset verify the advantage of the proposed method over some baselines.

### Strengths
1. Training data detection is an important problem to explore.

2. The proposed method does not need any reference model, which is easy to implement.

3. The experimental results show some advantage.

### Weaknesses
1. Only one dataset is used for experiments.

2. Please correct me if I am wrong. The proposed method seems to only applicable to LLMs which provide logits of outputs. Can it be applied to SOTA LLMs such as GPT-4 and Claud?

3. Please correct me if I am wrong. The proposed method seems to have difficulty in detecting the texts which are very well written or very badly written.

### Questions
See above review

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors primarly focus on tackling the problem of detecting examples included in a model's pretraining data, as opposed to the bulk of work focusing on detecting data pertinent to a downstream task. To this end, the authors introduce a benchmark dataset -- composed of wikipedia data known to be excluded from current published LLMs -- and a method for predicting if a sample has been seen by the model during pre-training. They compare the performance of their approach with several other known approach, and demonstrate that their approach outperforms the others, on their constructed benchmark dataset. (They also compare direct-examples versus paraphrased examples, though this is in the appendix.) The authors then apply their detection method in two case studies: 1) detecting books known to be included in ChatGPT training data, and 2) detecting data pertinent to downstream tasks. Through these case studies, the authors demonstrate that model size and text length are two important factors in the feasibility of detecting pretraining samples.

### Strengths
Although this is not at all my specific area of NLP, I thought the paper was a very nice read. It has a very concrete, and strong motivation for the investigation, and in general is very clearly written, such that I could easily follow the paper, despite this not being my specialty. The authors' proposed method (MIN-K PROB) was very simple and intuitive, and seems to work well across a number of settings (with the WikiMIA benchmark, and also the book and fine-tuning data experiments). I also liked that they included the baseline experiments with paraphrased data. The analysis throughout the paper was also typically very clear, reinforcing the role of model size and text length.

### Weaknesses
Because I found the paper mostly very clearly, I don't have much to say in terms of weaknesses :-). Thus, I will use this section to point out the instances that are a bit unclear, or otherwise areas I think should be addressed in some form (e.g. punctuation), though I know this does not really constitute "weaknesses".

Weaknesses: 

1. I presume the authors only work with English? That itself is not a weakness, of course, but it should be clearly stated. The "weakness" part of working with only English, is that I think lower-resourced languages may contradict the underlying hypothesis propping up the MIN-K PROB method: That is, because English is such a large percentage of training corpora for multilingual models, I'm not sure how this would work for other languages where the token probabilities given by LLMs are likely to be very low in general. How does this square with the authors' original hypothesis, and newly proposed method? 

Minor clarity issues: 

2. [S4.1] You say you use "different lengths (32, 64, 128, 256)", but do not specify what -- is this characters? tokens? words? S5.1 says "words" specifically. 

3. [S6.2] Similar to above: are your "examples" document level? Sentence level? Or what? 

4. [Figure 4] Your figure 4 makes it look as if 7 of the books are contaminated beyond 100%. I can tell from Table 2 that the books in the last bin (100-120) of figure 4 are at 100%, but I would either outright explain that the final bucket corresponds to 100% contamination, or change something with the visualization, because it looks a little funny :-). 

4. [S6.2] I find the verbiage around "in-distribution" and "outlier" contaminants to be a bit awkward. If I'm understanding you correctly, Fig5 (a) shows the contaminates that you correctly detect in the continued-pretrained model, (b) shows contaminated unrelated to the continued-pretrained model, but still included in pre-training. Is (a) the "outlier", simply because its not supposed to be included in pre-training data, and thus (b) is the "in-distribution" because this sort of data is presumed to be the type of thing we'd expect in pretraining data?  Maybe reword to "downstream task data" and "control data", or something of the like? 

Punctuation: 

5. [Appendix] Tables 5 and 6 have no bold numbers.

6. [Page 3, "Challenge 2", second paragraph] Missing a "." after the first sentence.

### Questions
1. (From "Weaknesses" Q1) Seeing as English is going to be much more sensitive in terms of word/token probabilities, what about non-English languages, that don't constitute so much of the PLM training data. If we take mT5 as a VERY ROUGH example of the distribution of representation across languages for LLM pre-training data: English represented roughly 5% of training data -- but what about all the languages that represent only a fraction of a percent of training data (e.g. Basque, Hausa, Amharic)? Will your proposed detection method still work for these instances, where the "signal" that each token 

2. (From "Weaknesses" Q4) This distinction between "in-distribution" (August 2023 Events Wikipedia) and "outlier" (downstream task datasets that ought nought to be in training) got me thinking -- do you think your approach will struggle with certain domains over others? Again, if we hark back to your original assumption about unseen data having more outliers w.r.t. probability from the LLM: I would expect books and such to have much more complicated (i.e. higher PPL) samples than, say, twitter posts.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is about speculating whether a piece of text has appeared in the pretraining corpus of an LLM or not. Authors prepare a corpus by crawling wikipedia. Their idea is to partition event pages into those before a certain date and those after the date, to obtain pages that have been or not been used in pretraining corpora.

They also report that for the texts that have not been used during the pretraining stage, word occurrence probabilities are lower, which is a simple heuristic.

Most of the paper is dedicated to reporting various creative experiments. Apart from experiments on the corpus, and on the proposed heuristic; a set of experiments on speculating the use of copyrighted books in the pretraining corpora of existing LLMs, and also another set of experiments on the possibility of detecting leaked training sets into the pretraining corpus.

### Strengths
Except in a handful of cases, the paper is well-written.\
A dataset will be released.\
The proposed heuristic works.

### Weaknesses
Not trying to undermine the amount of work done by the authors, but I feel the paper is packed with distracting experiments. I think the two case studies reported by the authors, which have taken up three pages, should be two blog posts, rather than three pages of an ICLR paper. In my opinion it is fine that the proposed method (or heuristic) is simple. But it is not fine to fill out the remaining pages with experiments which are either judgmental (the first case study) or repetitious (the second case study).

Page 8, second paragraph. Authors report that their accuracy is proportional to the pretraining corpus size. They also cite a paper on memorization of NNs, and argue that outliers are memorized better.
My question is: with the same theory, can Authors justify why the outliers of a small dataset are not memorized better than the outliers of a large dataset? Because that is what they are reporting. This cannot be supported by the cited theory.

My last question (and the most important one) is that why the proposed method works? Authors have not answered this pivotal question. Why not using the occurrence probability of all the words, why not the occurrence probability of the entire sentence, why not the occurrence probability of the sentences that appear in the pretraining corpus and filtering out the rest. "WHY" the proposed heuristic works?



### Questions
Page 3, Paragraph 6, what is x? It looks to be out of context.

In Section 6.1, you have a passage that starts with “main results”, and then after that you have another section called “Results and …”. Please merge these two.

Section 3, why are you using “negative log-likelihood”? In optimization people use it, because the derivative operator minimizes the loss function. You are not minimizing anything, so you do not need to say “negative …” to be forced to also say “the highest negative ….”. The same thing applies to Page 15, in your pseudo-code. Just say log-likelihood.

In Page 8, paragraph “Data occurrence”, it looks Authors are not aware that this is not a new finding. [1] reports comprehensive experiments on this subject.


[1] Large Language Models Struggle to Learn Long-Tail Knowledge. ICML 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method and benchmark to detect if a type of data appear in LLM pretraining. The main idea is to use the average of low probably of n (20 in the paper) tokens to gauge if the piece of text is used in pretraining. Paper is well-written and the idea is easy to follow.

### Strengths
- The author touched an interesting topic. The experiment looks solid. Paper is well-written and easy to follow.

### Weaknesses
 - The methodology sounds dubious. It doesn't take consideration of the data ordering in the training phase. For instance, in the paper, authors showed that learning rate affects the result a lot. In the late stage of training, the learning rate will be small which could impact how well model remember the data.
- It also doesn't consider the data distribution/mixture in the training. e.g. llama training duplicates wikipedia data. 
- High probability of a small piece of text doesn't mean that model is trained entirely on the content. The piece of text might appear somewhere else.  
- Lack enough of novelty

### Questions
- In section 5.2, it should be 50% of books have over 90% contamination? 
- The method used here doesn't take consideration of the data ordering in the training phase. For instance, as is shown in the paper that learning rate affects the prediction a lot. In the late stage of training, the learning rate would be small which could impact how well model remember the data.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
