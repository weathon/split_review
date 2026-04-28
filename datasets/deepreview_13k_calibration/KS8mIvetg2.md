# Proving Test Set Contamination in Black-Box Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Large language models are trained on vast amounts of internet data, prompting concerns and speculation that they have memorized public benchmarks. 
Going from speculation to proof of contamination is challenging, as the pretraining data used by proprietary models are often not publicly accessible.
We show that it is possible to provide provable guarantees of test set contamination in language models without access to pretraining data or model weights. Our approach leverages the fact that when there is no data contamination, all orderings of an exchangeable benchmark should be equally likely. In contrast, the tendency for language models to memorize example order means that a contaminated language model will find certain canonical orderings to be much more likely than others. Our test flags potential contamination whenever the likelihood of a canonically ordered benchmark dataset is significantly higher than the likelihood after shuffling the examples.
  We demonstrate that our procedure is sensitive enough to reliably prove test set contamination in challenging situations, including models as small as 1.4 billion parameters, on small test sets of only 1000 examples, and datasets that appear only a few times in the pretraining corpus.
  Using our test, we audit four popular publicly accessible language models for test set contamination and find little evidence for pervasive contamination.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a statistical test that given certain assumptions can indicate whether a black-box language model has been trained on certain datasets. This is a topic of increasing interest and importance given the prevalence of pretrained models that are trained on very large amounts of data.  The authors first propose a simple permutation test and identify some weaknesses with it. They then propose a more sophisticated sharded test. The authors show 2 kinds of experiments:

(1) They test on a dataset where they have injected a small amount of certain test sets to see if their approach can detect them.

(2) They apply their test to existing models such as Lllama-2 showing their approach can scale.

### Strengths
-Topic of large importance in the community given the direction of the field. 

-Novel approach with thorough empirical results. I have some questions about the definition of test set contamination below.

-Well written and interesting.

### Weaknesses
I have some questions about the definition of test set contamination below.

In Figure 1 the authors show test set contamination for BoolQ. But the examples there are unlabeled. Are the authors targeting unlabeled test set contamination i.e. the input is present in the pretraining data but not the label?

Would be great to have some justification and explanation of this setting.

### Questions
In Figure 1 the authors show test set contamination for BoolQ. But the examples there are unlabeled. Are the authors targeting unlabeled test set contamination i.e. the input is present in the pretraining data but not the label? 

Would be great to have some justification and explanation of this setting.

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
This paper studies the problem of identifying test set contamination in large language models, i.e., detecting that a test set is present in the pretraining data of a language model. The main idea behind the approach is that for test sets that have some canonical order of individual instances (e.g.: the order in which the dataset creators release the dataset), the likelihood of the test set in that order would be significantly higher than any random permutation of the dataset. Based on this idea, the paper proposes two versions of the test, one of which shards the test set and aggregates statistics over the shards to make the estimate more robust to potential biases in the model.

The tests are evaluated first by measuring their sensitivity when pretraining datasets are intentionally contaminated. It is shown that they are highly sensitive when the tests sets are large or have been duplicated enough in the pretraining data. The test is then used to measure contamination of the pretraining data used to train the Llama models and it is shown that the findings agree with prior reports.

### Strengths
This is clearly written paper and makes a strong contribution. The tests do not require access to model weights or pretraining data, making them practically useful.

### Weaknesses
The experiments do not compare the performance of the proposed tests to prior work. I understand that this work differs from say, the work from Carlini et al. in that this work focuses on set-level contamination, but how does aggregating instance-level statistics over a set compare?

- How sensitive is the proposed test to the model size?

### Questions
- How does the performance of this method compare to that of prior work (see Weakness)
- How sensitive is the proposed test to the model size?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the issue of test set contamination in large language models (LLMs), referring to the phenomenon where LLMs memorize public benchmarks during their pretraining phase. Since the pretraining datasets are rarely available, this paper proposes a statistical test to identify the presence of a benchmark in the pre-training dataset of a language model without accessing the model’s training data or weights. The intuition is the exchangeability of datasets— the order of examples in the dataset can be shuffled without affecting its joint distribution. If a language model shows a preference for any ordering of the dataset, it might have seen the data during pretraining. The test on the LLaMA-2 model identifies potential contamination in the MMLU benchmark, which is consistent with the results in the original LLaMA-2 report.

### Strengths
-	The idea of utilizing dataset exchangeability to identify test set contamination is novel and interesting. 
-	The proposed sharded likelihood comparison test addresses the tradeoff between statistical power and computational requirements of the permutation test, which is promising. The sharded rank comparison test also provides (asymptotic) guarantees on false positive rates.
-	Experimental results are promising. A GPT-2 model is trained from scratch on standard pretraining data and known test sets to verify the efficiency of the proposed method in identifying test set contamination. The method is also tested with an existing model, LLaMA2, on the MMLU dataset, showing general agreement with the contamination study results.

### Weaknesses
 - Although a more efficient sharded rank comparison test is proposed, the computational complexity is still considerable. For example, testing 49 files using 1000 permutations per shard can take 12 hours for LLaMA2.
- There is no comparison with other baseline methods.
- The method relies on a strong assumption of data exchangeability, which may not hold in real-world datasets.

### Questions
If a dataset is not exchangeable, how effective is the method?

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
This paper targets the problem of detecting test set contamination of black-box language models. The proposed method is based on two hypotheses: (1) the exchangeability of many datasets (distribution won't be affected after shuffling); and (2) if a language model is contaminated, it is more likely to find certain orderings of data samples than other orderings. Then a statistical test is proposed to compare the log probability of the dataset under the original ordering to the log probability under random permutations on sharded datasets. Experiments are conducted with one 1.4B-gpt2 model trained from scratch on 10 test sets, and the results prove the effectiveness of the proposed framework.

### Strengths
- This paper targets an interesting and exciting problem in the community, test set contamination. 
- Based on the hypothesis, this paper proposed a contamination detection method, which is intuitive and easy to deploy in other settings.
- The method is verified with a 1.4B language model trained from scratch, and the existing Llama2 model, both showing promising results even when the test set only appears a few times in the pre-training corpus.

### Weaknesses
 - I'm most concerned about the definition of contamination used in this paper. Currently, the most popular definition of contamination follows the n-gram analysis. In real-world scenarios when training large language models, it's hardly seen to directly feed original data samples in their original ordering as shown in Figure 1. The application of this work could be greatly limited.
- From Figure 3, it seems that the parameters for shards and permutations are sensitive and have to be carefully selected when being applied to other test sets.
- The paper only targets direct sentence appearance in the pre-training stage. What about instruction-tuning data in the SFT stage?

### Questions
- Could you further explain "high false positives" in existing n-gram-based analyses?
- How did you deal with the labels for the data samples in test sets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
