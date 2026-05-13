# A Simple Baseline for Predicting Future Events with Auto-Regressive Tabular Transformers

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Many real-world applications of tabular data involve using historic events to predict properties of new ones, for example whether a credit card transaction is fraudulent or what rating a customer will assign a product on a retail platform.
Existing approaches to event prediction include costly, brittle, and application-dependent techniques such as time-aware positional embeddings, learned row and field encodings, and oversampling methods for addressing class imbalance.
Moreover, these approaches often assume specific use-cases, for example that we know the labels of all historic events or that we only predict a pre-specified label and not the data’s features themselves.
In this work, we propose a simple but flexible baseline using standard autoregressive LLM-style transformers with elementary positional embeddings and a causal language modeling objective.
Our baseline outperforms existing approaches across popular datasets and can be employed for various use-cases.
We demonstrate that the same model can predict labels, impute missing values, or model event sequences.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a method, called STEP, for training decoder-only, LLM-style models for tabular data understanding tasks. The authors design a column-wise tokenization mechanism and use time-based data packing to preprocess rows of events in a table. They train the decoder with event features in arbitrary orders to simulate the masked language model (MLM) training used in other methods. Experiments across multiple datasets show that the proposed approach achieves good performance.

### Strengths
1. Design of using a decoder-only LLM with a causal language modeling objective to encode and predict tabular data is new.
2. The authors conduct experiments on a variety of datasets and tasks, where the method achieves better performance than two tabular transformer baselines.

### Weaknesses
1. Unclear Motivation: The motivation for using a decoder-only architecture for encoding-style tasks is not well-explained. The authors simulate MLM training with features in arbitrary orders, which raises the question of why an encoder-based architecture and traditional MLM training weren’t used directly. If performance was the factor, then the results in Table 1, where LLaMa performs the worst, might indicate that a decoder-type transformer isn’t optimal for these encoding tasks. While STEP performs better than the baselines, baseline performance is quite low. Were the baseline results reported after equivalent fine-tuning on the same amount of training data?

2. Vocabulary Use: It is unclear how separate vocabularies are used during training. Why not simply use a single tokenizer and a unified vocabulary by assigning different IDs to identical values from different columns? The paper mentions separate vocabularies, but it is unclear if this implies separate tokenizers or a single tokenizer with non-overlapping ID ranges. This distinction is important for understanding the implementation details and potential limitations.

3. Experiment Details: Key experimental details are missing. For instance, the configuration for the base LLM is not specified — is the model a pre-trained LLM or randomly initialized? If pre-trained, an ablation study comparing performance before and after your training would have been necessary. Also, the vocabulary size of 60,000 tokens is ambiguous—does that mean STEP only has ~60,000 unique numbers? The paper does not clarify how numerical features are handled, especially given that many tabular datasets contain a wide range of numerical values.

4. Weak Baselines: There are more advanced models for handling tabular or structured data, such as GPT-4o, Claude, TableGPT, and code models like CodeLlama or CodeQwen. A more comprehensive comparison with these stronger baselines would be more convincing. The current baselines, while perhaps standard in some tabular settings, do not represent the state-of-the-art in large language model capabilities for structured data.

5. The proposed method requires separate training for each task or dataset, which is not general. Details on training time and GPU requirements are missing as well. The lack of information on computational resources and training time makes it difficult to assess the practical applicability of the proposed method.

### Questions
Which decoder-only LLM is used for training? Is it a pre-trained LLM or a randomly initialized model? How many layers are in the model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a simple yet flexible baseline model for tabular event data, utilizing standard autoregressive, LLM-style transformers capable of addressing a variety of use cases involving different data types and tasks.

### Strengths
The authors' intention to create a versatile baseline model tailored for tabular event data is commendable and has the potential to accelerate advancements in this field.

### Weaknesses
The experimental section is somewhat lacking. Beyond Table 1, the authors should conduct additional experiments to showcase various aspects of the proposed model and provide a more comprehensive comparison with existing models, which I believe is essential for baseline papers. Furthermore, Figure 4 conveys limited information, making it seem unnecessary.

### Questions
- In line 386, is the caption of Table 1 incorrectly labeled? Why is it titled 'Summary of experimental configurations for different datasets'?
- In line 327, there are two occurrences of 'with.'

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to model event streams using a standard autoregressive, decoder-only Transformer (like the ones used in modern LLMs).  Event streams are unique compared to time series data in that the events may occur at arbitrary timestamps.  It is also notable that in event stream applications, key covariates/features may be missing within the context window.  In this paper, the approach is to “flatten” multivariate tabular event data into a single sequence of tokens, where features/fields of individual events (individual “rows”) occur as a sub-sequence (of tokens) within a larger, ordered-by-time sequence-of-subsequences over all the events.  In order to model the arbitrary arrival times of events, this paper proposes encoding the inter-arrival duration as a numeric feature (binned into one of 32 bins for tokenization).  To handle specific missing features, this paper proposes to mask all of the target features in the context window during training (or the system could be re-trained from scratch with partially-masked labels, although it does not perform as well on the evaluation tasks if this is done).  Finally, to enable predicting arbitrary features/fields of individual events using a single model, the paper proposes creating multiple versions of training sequences, each with the fields in a random order WITHIN each event sub-sequence.  A single model can be trained over all the randomized orderings collectively.  The proposed method shows competitive accuracy with two prior approaches on a few prior tasks.

### Strengths
Using vanilla Transformers to model event data is a good idea.  LLMs are already being trained on multi-modal data, either implicitly by consuming data of different types (including tabular data) from the web, or explicitly by being fed speech, image, video, and other modalities during training.  Prior work has shown LLMs can already be used to predict time series data out-of-the-box without any special fine-tuning.  It seems modeling events will be within the capabilities of foundational models in short order.  As such, this paper is on the right track.

The writing within each section is fairly clear.  Figure 1 is helpful.  Figure 4, 6, and 7 are good things to test.

### Weaknesses
Overall, it seems like if this approach is being positioned as a simple baseline that nevertheless works quite well on a range of tasks compared to other approaches, then the empirical evaluation needs to be much more extensive and rigorous and convincing.  I also feel like it’s a missed opportunity: since STEP uses its own vocab and whatnot, it doesn’t seem capable of leveraging *pre-trained* LLMs (e.g., fine-tuning them to work on event stream data).  It would have been useful to investigate the possibility of training event predictors using tokenization, etc., that is COMPATIBLE with LLMs, and maybe even use the LLMs directly to do the prediction, along the lines of what Gruver et al. did for time series forecasting.

Experimentally, it was difficult to put the results in context or understand what was done:

- What is the random baseline on each task?  I assume Table 1 is accuracy?  Wouldn’t precision/recall make more sense for a low-frequency detection task like detecting fraudulent transactions?  Especially since no steps were taken to address data imbalance. The results suggest STEP is much, much worse than TabBERT or FATA-Trans on the credit card data (19x the error), but the way the results are presented do not make this very clear, nor suggest what is going on (does STEP predict “non-fraudulent” in all cases?  We don’t know from Table 1).
- How are the error bars determined in Table 1?
- It seems like STEP is very sensitive to the things that give it unique capabilities.  E.g., when randomizing, the error rate on the credit card data increases significantly.  Also, Section A.1.1 shows that STEP with partial masking is worse than the baselines across all tasks.  This sensitivity isn’t really explained in the paper.  The brittleness of prior work is emphasized in the paper abstract, but STEP also seems hard to recommend for use out-of-the-box.

Also, as this is event stream prediction, it’s notable there is no evaluation of predicting the inter-arrival times of events:

- How accurately can STEP predict time-to-event?  How important is time as a feature?  What if you removed it entirely?
- What do you lose by not knowing the absolute time? (e.g., not knowing whether an event occurs on a weekend or not)
- Is 32-bins enough for numeric data?  What about 64?  Or 16?

Some other natural questions are not considered or not explained clearly:

- “We came to these hyperparemeters [sic] through trial and error across multiple runs” – but there’s no mention of a separate dev/validation set for hyperparameter tuning. Did you tune the HPs on the test data?
- You mention “Event Stream GPT (ESGPT), an open-source library designed to streamline the end-to-end process for building GPTs for continuous-time event sequences” – but can’t we just use ESGPT as the baseline for event stream prediction?  Why do we need STEP, another baseline?  Does STEP work better than ESGPT for some reason?
- Transformers are known to be very “data-hungry”.  How does accuracy here depend on the amount of training data?
- Why does this method improve over the prior art on ELECTRONICS and MOVIES?  Are we sure we used the exact same train/test splits?  Did they really both use exactly length-10 sequences, the same as in this work?  Do we use the same data splits?
- How could we handle predicting a label on an event based partly on future *events*?  E.g., say someone purchased jewelry with the credit card (maybe fraud?) and then next they purchase a coffee, then got a subway token, etc.  Could those future purchases be used to influence our assessment of the jewelry purchase?

The paper is also a bit disorganized.  For example, the baseline systems are described in the methodology section, but not in experimental details, except the Llama baseline, which is introduced in “Results”.  Data preprocessing is mentioned in 3.3 but also the same example is used in 4.2.  So I found myself having to jump around a bit to get the details.  It took me a long time to go back and find where the paper mentions that it uses “time since last event” rather than the absolute timestamp (it wasn’t in 3.1 and 3.2, which discuss encoding time, but rather it was in 4.2).

Finally, I find this work lacks an understanding of what an autoregressive generative model is, i.e., a joint model over the data, factorized in a certain manner.  Autoregressive transformers are just used here as a tool.  So it’s a very applied solution.  A more theoretical understanding could help connect things here to prior generative models.  E.g., the idea of being able to impute missing data in different orders has been explored before – e.g., it’s similar to what is done in MADE/NADE – See Uria et al., https://arxiv.org/abs/1310.1757 for the re-orderings, also used in MADE, Germain et al., https://proceedings.mlr.press/v37/germain15.html.

Things that do not affect the review scores:

- Normally figures in papers are so small, but here it seems like Figure 4 is *unnecessarily large*
- Regarding the synthetic credit card data, in the TabGPT paper it says, “the transactions are created using a rule-based generator where values are produced by stochastic sampling techniques, similar to a method followed by [19].”  But in this paper, it suggests this dataset was made via TabGPT itself: “additionally, Padhi et al. (2021) produces the widely used synthetic credit card transaction dataset by training a causal decoder on top of TabBERT (appropriately called TabGPT).”
Typos start creeping up near the end of the paper:
- “task of predicting if a client with with leave the bank”
- “The each record is separated by a token that delineates new events within the sequence.”
- “we explore how masking some or all of the prior event label during allows the model”

### Questions
Note quite a few questions are noted above under Weaknesses.

“Additionally, because we use a word-level tokenizer the maximum vocab size is 60000” – please explain.

5.3 – if you pass in fewer events (e.g., shorter sequence lengths in Figure 4), I don’t get why the model would predict a label at all.  Like, didn’t we mask out all the labels for the first 9 events?  Wouldn’t it only predict a label for the 10th event?

Since you can randomize the order of the observed features, can you do better by averaging over multiple re-orderings or feature subsets?  E.g., say you are predicting column D and you’ve seen only A, B, C.  Can you predict A, C, B, <>, and B, A, C, <>, and C, B, A, <>, etc?  This also connects to the MADE/NADE work.

### Soundness
2

### Presentation
2

### Contribution
1
