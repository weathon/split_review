# Contextual Biasing with the Knuth-Morris-Pratt Matching Algorithm

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3

## Abstract
Contextual biasing refers to the problem of biasing the automatic speech recognition (ASR) systems towards rare entities that are relevant to the specific user or application scenarios.
We propose algorithms for contextual biasing based on the Knuth-Morris-Pratt algorithm for pattern matching. During beam search, we boost the score of a token extension if it extends matching into a set of biasing phrases.
Our method simulates the classical approaches often implemented in the weighted finite state transducer (WFST) framework, but avoids the FST language altogether, with careful considerations on memory footprint and efficiency on tensor processing units (TPUs) by vectorization. Without introducing additional model parameters, our method achieves significant word error rate (WER) reductions on biasing test sets by itself, and yields further performance gain when combined with a model-based biasing method. % leads to new state-of-the-art biasing accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of contextual biasing for speech recognition. The paper proposes to use very popular and efficient KMP algorithm used for pattern searching to bias the ASR decodes with the contextual terms. 

Experimental results on the enterprise model and real/TTS audio show usefulness of this approach.

### Strengths
The paper clearly demonstrates the applicability of KMP's efficiency on the biasing task.  

The paper reads well and is easy to follow.

### Weaknesses
1. The paper lacks adequate references to the related work in the area of the contextual biasing for ASR Models. I have added some relevant citations.

2. Lack of comparison on publicly available data and models limiting reproducibility. Le at al 2021a [2] provides an open protocol for evaluating on librispeech corpus (https://github.com/facebookresearch/fbai-speech/tree/main/is21_deep_bias).

3. Lack of comparison with baselines, how well does this model compare against a simple shallow fusion with an external n-gram trained on the dictionary items for the cases with prefixes? Comparison against the Neural baselines such as NAM and other relevant works from the literature are missing.

### Questions
1. In this work, the bonus score is added each time the match happens, how do you address the scenario where prefix has matched but suffix won't match and the hypothesis are still carrying extra weight provided during the biasing?
E.g, if the dictionary item is TWIN and the actual audio has TWENTE, but the hypothesis is preferring TWIN (and/or its continuations) due to additional biasing. 

2. What are the RTF scores for this method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is about contextual biasing for automatic speech recognition (ASR).

Contextual biasing means: Consider Google Home or Alexa, where it is common to play songs, or maybe call someone from the contact list. So when the user speaks, the probability for such words of recently played songs or from person names from the contact list are higher than for other users, and contextual biasing will use that knowledge and boost the scores in the beam search recognition for such words or phrases.

Contextual biasing is not new, and many previous solutions to this exist. In this paper, a new method is proposed, to improve the beam search specifically. The ASR model is not changed. More specifically, the authors propose to use the Knuth-Morris-Pratt algorithm as an efficient way to find biasing phrases in the hypotheses and then boost them.

The Knuth-Morris-Pratt (KMP) algorithm is an algorithm to search for a substring in a given string in an efficient manner. The naive implementation would take O(n * m), n being the long string length, m being the substring length, while KMP can do it in O(n + m).

This provides an alternative formulation to the weighted finite state transducer framework, which conceptually does the same. However, they also use an efficient TPU-friendly implementation of this specific algorithm.

The experiments show that the KMP method on its own performs slightly worse than another model-based biasing method, namely the neural associative memory (NAM). However, KMP and NAM combined give improvements over NAM alone.

### Strengths
They show how to apply the KMP algorithm inside beam search to boost the biasing phrases.

The experiments show that the proposed KMP-based algorithm gives nice improvements when used together with NAM in the setting biasing.

### Weaknesses
The topic is very ASR specific. I'm not sure if the broader ICLR community is interested in this, and some conference like Interspeech or ICASSP would be a better fit?

In principle, the method could be applied for other tasks, for example for machine translation. However, this is not investigated here. I think this would make it a better fit for ICLR.

It is explained that the proposed method is conceptually similar (or the same?) as WFST-based approaches. However, in the experiments, it is not compared.

The argument is about KPM being TPU friendly. However, if WFST is conceptually equivalent, how can it be different? It's just a matter of implementation then. This is either stated confusingly, that it is in fact different. Or it is stated confusingly that they are the same, and you can also use the WFST formulation to describe exactly the same algorithm. In any case, it's a bit confusing. So then using the WFST-based formulation, you could just use the equivalent algorithm, and it would also be TPU friendly. In any case, this should be clarified.

The argument about being TPU friendly again: Actual speed performance is not really compared. How much worse does the WFST-based approach perform?

Code is not released?

With increased B (number of biasing phrases), the result gets worse. First to clarify: The test dataset is designed such that the word from reference transcription is always in the biasing phrases? Or otherwise, why would it get worse with increased B? And then: in practice, how big would B be? And how to update the set of biasing phrases? Wouldn't a test make more sense which is more close to how this is actually used in production?

### Questions
Abstract:

> Our method simulates the classical approaches often implemented in the weighted finite state transducer (WFST) framework, but avoids the FST lan- guage altogether, ...

I'm not sure what this means. Does this mean, it is actually equivalent to what is being done with the WFST framework, and only a reformulation/reinterpretation? So the novelty here is no new method, but just a new interpretation of the existing algorithm? Or is this really different? Why is it relevant to avoid the FST language? What is the actual difference when you don't avoid the FST language, i.e. when you look away from just rephrasing things.

Also, why would you want to avoid the FST language? The FST language is very simple, while the presented algorithms actually look more complicated? Maybe it would actually be helpful to not avoid the FST language, but to present the proposed method within the FST language, so that it is easier to see the actual differences, and also easier to understand.


Section 3 (but same thing also said in intro and elsewhere):

> While they [FSTs] can be represented as graph with sparse adjacency matrices, in general FSTs are not efficient to use on TPUs which are optimized for dense operations. Our work is one step towards incorporating FST functionalities into a TPU-friendly implementation.

I'm not sure if this is really about FST or not. Couldn't you reformulate the presented work also as an FST, and then this statement would be false?


I'm not sure if the paper is a bit too ASR specific? What about applying this also to machine translation or other tasks?


Runtime differences between OTF Rescoring, Fusion F = 10, Fusion F = 50, Fusion F = 4096? And the same also with NAM?


Is the code released? If not, this would be a major weakness of the work.


With increased B (number of biasing phrases), the result gets worse. First to clarify: The test dataset is designed such that the word from reference transcription is always in the biasing phrases? Or otherwise, why would it get worse with increased B? And then: in practice, how big would B be? And how to update the set of biasing phrases? Wouldn't a test make more sense which is more close to how this is actually used in production?

On TPU, what is actually parallelized? I assume, in Algorithm 2, the loop over B is parallelized? Ok, yes, you write that in the text (end of Section 2.2). It would be nice to specifically mark this in the algorithms, e.g. write "vectorized-for" or so. E.g. also in Algorithm 3, the loop over the hypotheses and also over the k=1...F would also not really be a loop but run in parallel (I assume).

Comparison to WFST-based biasing?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method for contextual biasing of speech recognition (ASR) at decode time. The usual practice is to build a WFST for the biasing phrases and use this in a kind of shallow fusion strategy during decoding. The authors posit that such a method is inefficient on TPUs, and hence propose an equivalent string matching technique based on Knuth-Morris-Pratt (KMP) algorithm. They show that this method provides significant improvements in WERs for utterances containing biasing phrases, without causing large degradations when they are not present.

### Strengths
1. Contextual biasing in ASR is an important application. As mentioned by the authors (Section 3), biasing can be done at the decoding level or at the model level — the proposed KMP algorithm operates at the former, showing good WER improvements. It is also shown to be complementary to model-based biasing (using NAM).

2. The authors have discussed the parallelized time and space complexities of the proposed methods wherever applicable.

3. On the Contact-Tag data, the WER is improved from 14.7% to 7.7% (for KMP) and 3.0% (for NAM + KMP), which is quite a large improvement. At the same time, the WER for “anti-biasing” only degrades from 1.7% to 2.3% and 2.5%, respectively.

### Weaknesses
### Motivations misaligned with application and results

The main objective of the paper is to build a contextual biasing system that is efficient to decode on large-scale parallelizable infrastructure such as TPUs. However, in the introduction and the experiments, the application of the method is for recognizing contact names for voice assistants. In my understanding, such voice assistants are commonly placed on the edge device, which does not usually have built-in TPUs. As such, it is hard to see what would be the impact of the proposed method from a decoding efficiency perspective.

Even if we ignore the above, it is hard to buy into the “efficiency” argument, since the authors do not provide any RTF results to back their claims. “Memory footprint” and “efficiency on TPUs” are essential motivating factors behind the proposed method, but the evaluation is only conducted for quality (WERs). In fact, it appears that the stated TPU-based vectorization is essentially just parallelization of a loop over all biasing phrases — it is hard to see why such parallelization would be TPU-specific.

Throughout the paper, the authors have mentioned that FST-based biasing poses challenges for efficient TPU-based implementation. Recently, FSTs have been efficiently represented and manipulated on GPUs using specialized kernels (see the GTN and k2 projects). In fact, the Aho-Korasick algorithm has recently been used for contextual biasing on GPUs and released in the “icefall” library. Why are these methods not applicable for TPUs?


### Problems with evaluation design

I am concerned about the lack of public benchmarks or baselines in the experiments. The authors use in-house voice-assistant data from a previous work (which is not publicly available AFAIK) to conduct their evaluations, and do not release code for their method. This would make it impossible to replicate or verify the reported improvements. There are also no comparisons with any other decoding-based contextual biasing methods, although the authors seem to be quite aware of their existence (Section 3). Granted, the proposed KMP algorithm should be equivalent to the WFST-based shallow biasing approach proposed earlier, but it would be good to show this as a sanity check. It would also be useful to show how the memory requirement of the WFST-based implementation versus KMP change with increase in the size of the biasing list; the latter is absolutely essential, since this is the main motivation for using this algorithm.

### Presentation

The description of the proposed method is very dense, and may benefit from some abstraction. Contextual biasing is formulated into two stages: (i) pattern matching, and (ii) boosting matched patterns. The authors should consider presenting the two parts independently (instead of the current presentation where (ii) builds on (i)). This would also be useful to think about other algorithms for (i) and (ii) without disturbing the other.

Second, the authors rely too much on Algorithm blocks to present their method (there are 5 in total including the appendices), which breaks the flow of reading and makes the paper hard to parse. It may be beneficial to release open-source code for the details of the algorithm and use more of the space to discuss the algorithms themselves, their connections with other contextual biasing methods, and their advantages/limitations.

### Questions
1. In Section 1 (under “Our contributions”), the authors state that their method “can be potentially useful for other sequence transduction tasks.” Can the authors describe what other tasks may benefit from sequence matching?

2. There are several linear-time algorithms for pattern matching such as Rabin-Karp, Boyer-Moore, etc. It would be useful to include a discussion about why KMP is most appropriate for the task.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
