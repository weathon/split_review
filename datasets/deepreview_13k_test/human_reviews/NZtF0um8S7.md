# Exploiting the Potential of Seq2Seq Models as Robust Few-Shot Learners

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
In-context learning, which offers substantial advantages over fine-tuning, is predominantly observed in decoder-only models, while encoder-decoder (i.e., seq2seq) models excel in methods that rely on weight updates. Recently, a few studies have demonstrated the feasibility of few-shot learning with seq2seq models; however, this has been limited to tasks that align well with the seq2seq architecture, such as summarization and translation. Inspired by these initial studies, we provide a first-ever extensive experiment comparing the in-context few-shot learning capabilities of decoder-only and encoder-decoder models on a broad range of tasks. Furthermore, we propose two methods to more effectively elicit in-context learning ability in seq2seq models: objective-aligned prompting and a fusion-based approach. Remarkably, our approach outperforms a decoder-only model that is six times larger and exhibits significant performance improvements compared to conventional seq2seq models across a variety of settings. We posit that, with the right configuration and prompt design, seq2seq models can be highly effective few-shot learners for a wide spectrum of applications.
~\blfootnote{* Indicates equal contribution}
~\blfootnote{\dag Work done at Kakao Corp., correspondence to jihyeonl@nvidia.com and dannykm@khu.ac.kr}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper performs a first-ever extensive experiment comparing the in-context few- shot learning capabilities of decoder-only and encoder-decoder (seq2seq) models on a broad range of tasks. The authors further propose two methods to more effectively elicit in-context learning ability in seq2seq models: objective-aligned prompting and a fusion-based approach. They show their methods significantly outperform decoder-only models.

### Strengths
+ This work develops an in-context evaluation toolkit for seq2seq models and conduct extensive experiments to investigate the performance of seq2seq models in zero-shot to few-shot scenarios.

+ The author explore prompting strategies and fusion-based approaches in encoder-decoder models, which reveals their ability of zero/few-shot learning.

+ The comprehensive experiments of comparison between decoder-only and encoder-decoder models could be very useful for researchers in this field.

### Weaknesses
- The technical novelty of this work is a bit weak. The proposed objective-aligned prompting and fusion-based approach are straightforward.

- The detailed description of the objective-aligned prompting method is missing.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper pays attention to the in-context few-shot learning capabilities of seq2seq models. Specifically, this paper conducts comprehensive experiments with an in-context evaluation toolkit to investigate the performance of seq2seq models in few-shot scenarios. In addition, an objective-aligned prompting strategy and a fusion-based approach are proposed. Through extensive experiments, some interesting conclusions are also obtained.

### Strengths
1.	This paper is well organized and easy to follow. 
2.	The motivation is reasonable and experiments are abundant.
3.	The findings and conclusions about in-context few-shot learning capabilities of seq2seq models will be interesting to the community.

### Weaknesses
Several main concerns are as follows:

1.	This paper claims that the objective-aligned prompting strategy is its one key contribution. However, this strategy seems to be very straightforward and some recent state-of-the-art works have already introduced such a strategy. In this sense, this contribution is somewhat limited.

2.	The second contribution of this work is a fusion-based approach, which also comes from the existing works, such as RAG and Fid. Therefore, what’s the main difference and contribution of this work? In addition, in the abstract, the sentence “our approach outperforms a decoder-only model that is six times larger…” shows that the proposed models will be much larger than the competitors. Is it not a significant limitation? 

3.	Can we consider the proposed fusion-based approach as a simple ensemble strategy? If so, the authors may need to explain more for this part.

4.	Are there any evidences to support the hypothesis in the sentence of “We hypothesize that the encoding of relations between demonstrations does not significantly impact in-context learning performance.”?

### Questions
Please kindly refer to the above comments.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
An extensive evaluation of zero-shot to few-shot performance of seq2seq models across a wide range of evaluation set is presented. The authors make a case for strong seq2seq model performance for generation and understanding tasks when compared to decoder only models.

### Strengths
The primary strength of this works seems to come from experimentally demonstrating that the seq2seq model can outperform the decoder-only model with 6 times larger parameters across diverse datasets.

### Weaknesses
Would've liked to see some evaluations around more varied generative tasks like Math/Coding which are more practically useful.

### Questions
Are there any tasks where the seq2seq few shot performance was inferior to decoder only models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the potential of Seq2Seq models as robust few-shot learners. A few studies have demonstrated the feasibility of few-shot learning with seq2seq models; however, this has been limited to tasks that align well with the seq2seq architecture, such as summarization and translation. The paper proposes two methods to more effectively elicit in-context learning ability in seq2seq models: objective-aligned prompting and a fusion-based approach. Remarkably, the approach outperforms a decoder-only
model that is six times larger and exhibits significant performance improvements compared to conventional seq2seq models across a variety of settings.

### Strengths
1. This paper is well-written regarding the language and organization.
2. The experimental evaluation validates their claims.
3.  The paper performs few-shot learning on a variety of tasks, indicating that the seq-to-seq model can have certain advantages, which is indeed a contribution.
4. Their analysis in the experimental parts is comprehensive.

### Weaknesses
1. The paper might want to explain a bit more about the specific tasks of few-shot learning.
2. The paper should explain why the seq-to-seq model is powerful in related tasks, from a machine-learning perspective.
3. Similarity, the paper might want to analyze in-depth why early fusion sometimes yields better performance than late fusion, from a machine-learning perspective.

### Questions
No other question, but the model proposed seems too simple. However, the experimental analysis and finding is nontrivial.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
